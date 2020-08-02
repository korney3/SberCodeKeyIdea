<template>
	<div>
		<div class="row">
			<div class="col-4">
				<input type="text" v-model="team.name" class="form-control form-control-lg form-control-hidden" placeholder="Название группы">
				<autosizetext class="form-control form-control-sm form-control-hidden" placeholder="Комментарии" v-model="team.desc"></autosizetext>
			</div>
			<div class="col">
				<autosizetext class="form-control form-control-sm mt-2" placeholder="Ключевые слова" v-model="team.keywords"></autosizetext>
			</div>
			<div class="col-auto">
				<button class="btn btn-outline-danger btn-sm mt-2" @click="$emit('del', team)">Удалить</button>
			</div>
		</div>

		<hr>
	</div>
</template>

<script>

import autosizetext from '@/components/autosizetext'

export default {

	props: ['team'],
	components: {
		autosizetext
	}
}
	
</script>

<style>
	.form-control.form-control-hidden {
		border: none !important;
		background: none !important;
		outline: none !important;
		box-shadow: none !important;
		padding-left: 10px !important;
	}
	.form-control.form-control-hidden:hover {
		background: #fff !important;
	}
</style>