<template>
	<div>
		<h1>Тестирование модели</h1>

		<button class="btn btn-primary mb-1" @click="generate">Загрузить случайный текст</button>


		<div class="row">
			<div class="col-7">
				<textarea class="form-control mb-2" rows="13" v-model="msg">
					
				</textarea>
				<input type="text" class="form-control mb-2" v-model="url">
				<button class="btn btn-primary" @click="think">
					<span v-if="!status_loading">Анализировать</span>
					<!-- <div class="spinner-border text-light" role="status">
					  <span class="sr-only">Loading...</span>
					</div> -->
					<span v-if="status_loading">...</span>
				</button>
			</div>

			<div class="col">
			
				<h3 v-if="res_teams && res_teams.length">
					Команды <br>
					<div class="badge badge-primary m-1" v-for="team in res_teams">{{team}}</div>
				</h3>

				<h5 v-if="res_keywords && res_keywords.length">
					Ключевые слова <br>
					<div class="badge badge-info m-1" v-for="keyword in res_keywords">{{keyword}}</div>
				</h5>

				<h5 v-if="res_tonality">
					Тональность <br>
					<div class="badge badge-danger m-1" v-if="res_tonality == 'Negative'">{{res_tonality}}</div>
					<div class="badge badge-success m-1" v-if="res_tonality == 'Positive'">{{res_tonality}}</div>
				</h5>

				<small><pre>{{res}}</pre></small>

				
			</div>
		</div>
		
		<br>
		<small><pre>{{clear_teams}}</pre></small>
	</div>
</template>



<script>

var demo_text = 'Уважаемые разработчики программы, каждый раз при входе в приложение Сбербанк онлайн на значке диалоги горит красный значок о непрочитанному сообщении в то время как непрочитанных сообщений там нет! К чему это делается? Или это Ошибка программы? Решите её пожалуйста! Очень раздражает! После моего обращения к вам по поводу горящего окна сообщений в приложении прошло уже два обновления. Проблема не решена. Каждый раз при входе в мобильное приложение горит красным цифра 1 на флажке сообщений. Непрочитанных сообщений нет! Исправьте пожалуйста эту ошибку!!';

// {
//   "keywords": [
//     "непрочитанный сообщение",
//     "каждый раз",
//     "сообщение",
//     "программа",
//     "приложение",
//     "ошибка",
//     "вход",
//     "уважаемый разработчик",
//     "мой обращение",
//     "мобильный приложение",
//     "красный цифра",
//     "красный значок",
//     "два обновление",
//     "флажок",
//     "сбербанк",
//     "проблема",
//     "повод",
//     "окно",
//     "значок",
//     "е",
//     "диалог",
//     "время"
//   ],
//   "teams": [
//     "Мессенджер",
//     "Global Navigation",
//     "Текстовый чат"
//   ]
// }

import axios from 'axios'

export default {
	data() { 
		return {
			url: 'http://345f947727a5.ngrok.io?topn=3&text=',
			msg: demo_text,
			res_teams: [],
			res_keywords: [],
			res_tonality: '',
			res : '',

			real_msgs: [],

			teams: [],

			status_loading: false
		}
	},
	created() {

		axios.get('./static/ios-3.json').then(res => {
		// axios.get('http://vispstudio.ru/sber/ios-3.json').then(res => {
			this.$set(this, 'real_msgs', res.data)
		})

		axios.get('http://nerpa.vispstudio.ru/storage/api.php?id=sberdevteams&op=get_db').then(res => {
				 // this.teams = res.data;

				 this.$set(this, 'teams', res.data)

			})

	},
	computed: {
		clear_teams() {
			let res = {}

			this.teams.forEach( x => { 
				res[x.name.trim()] = x.keywords.split(',').map(a=>a.trim()).filter(a=> a != '')
			} );

			return res;
		},
	},
	methods: {
		generate() {
			let id = Math.round(Math.random() * this.real_msgs.length);
			this.msg = this.real_msgs[id].title + "\n" + this.real_msgs[id].user_text;
		},
		think() {
			// alert('think');
			this.status_loading = true;
			let url_q = this.url + '"' + this.msg.replace('"','') + '"'

			axios.get(url_q).then(res => {
				this.res = res.data
				this.res_teams = res.data.teams
				this.res_keywords = res.data.keywords
				this.res_tonality = res.data.tonality



				// this.res_teams.concat( res.data.BERT.cosine_team )
				this.res_teams.push( res.data.BERT.cosine_team )
				this.res_teams.push( res.data.BERT.euclid_team )
				this.res_teams.push( res.data.FLAIR.cosine_team )
				this.res_teams.push( res.data.FLAIR.euclid_team )

				this.res_teams = this.res_teams.filter( (value, index, self) => { 
				    return self.indexOf(value) === index;
				} )

				this.status_loading = false;
			}, er => {
				this.status_loading = false;
			})

			// this.res_teams = ['ios msg', 'problem'];
			// this.res_keywords = ['ios msg', 'problem'];
		}
	}

}

</script>

<style>
	.badge {
		text-align: left;
    	white-space: normal;
	}
</style>