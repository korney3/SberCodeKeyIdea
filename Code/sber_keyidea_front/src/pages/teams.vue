<template>
	<div>
		<h1>Команды</h1>

		<p>Базовые наборы ключевых слов для команд и других групп</p>

		<button class="btn btn-primary" @click="add">Добавить группу</button>
		<br>
		<br>

		<team v-for="team in teams.slice().reverse()" :key="team.id" :team="team" @del="del"></team>

		<button v-if="is_new_db_json" class="btn btn-primary btn-block btn-lg btn-fix-bottom" @click="save">Сохранить</button>

		<br>
		<br>

		<small><pre>{{clear_teams}}</pre></small>

		<br>

	</div>
</template>


<script>

	import axios from 'axios'
	import team from '@/components/team'

	export default {
		data() {
			return {
				teams:[],
				old_db_json: '',
			}
		},
		created() {
			// axios.get('http://nerpa.vispstudio.ru/storage/api.php?id=sberdev&op=json').then(res => {
			// 	this.teams = res.data.teams
			// })
			axios.get('http://nerpa.vispstudio.ru/storage/api.php?id=sberdevteams&op=get_db').then(res => {
				 // this.teams = res.data;

				 this.$set(this, 'teams', res.data)

				 this.old_db_json = this.db_json
				// this.teams = res.data.forEach(x => x.desc = x.zones.map(a=>a.title).join(";\n") )
				// this.teams = res.data.forEach(x => x.team_desc = x.zones ? x.zones.length : '' )
				// this.teams.map(x => { 
				// 	x.desc = x.zones.map(a=>a.title).join(";\n"); 
				// 	x.keywords = x.team_key_words; 
				// 	delete x.zones; 
				// 	delete x.team_desc; 
				// 	delete x.team_key_words; 
				// } )
			})
		},
		methods: {
			save() {
				axios.post('http://nerpa.vispstudio.ru/storage/api.php', this.teams,  {
                    params: {
	                        op: 'set_db',
	                        id: 'sberdevteams',
	                        r: Math.random(),
                        }
                    })
                .then( 
                    response => { 
                    	this.old_db_json = this.db_json
                    },
                    error => { reject( error ) },
                );
			},
			add() {
				// alert('123')

				let max_id = Math.max.apply(Math, this.teams.map( o => o.id ))
				let item = {}
				item.id = max_id > 0 ? max_id + 1 : 1 ;
				item.name = '';
				item.keywords = '';
				item.desc = '';

				this.teams.push(item)
			},
			del( team ) {
		        let index = this.teams.indexOf( team );
		        this.teams.splice(index, 1);
			}
		},
		computed: {
			clear_teams() {

				let res = {}

				this.teams.forEach( x => { 
					res[x.name.trim()] = x.keywords.split(',').map(a=>a.trim()).filter(a=> a != '')
				} );

				return res;

				// return this.teams.map(x=> ({ name:x.name, keywords:x.keywords }) );
				// return this.teams.reduce( (previousValue, currentItem, index, arr) => { 
					// return previousValue[ index ] = 1
					// previousValue[ currentItem.name ] = currentItem.name
					// return previousValue
					// return previousValue[ currentItem.name ] = currentItem.keywords
				// 		// name:x.name, keywords:x.keywords 
				// }, [] );
			},
            db_json() {
                return  JSON.stringify(this.teams);
            },
            is_new_db_json() {
                return this.old_db_json != this.db_json;
            }
		},
		components: {
			team
		}
	}


</script>

<style>
	.btn-fix-bottom {  position: fixed; bottom: 0; left: 0; right: 0;  }
</style>