<template>
	<div>
		<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
			<div class="container">
			  <router-link to="/" class="navbar-brand" exact-active-class="active">
	                Сбербанк.Отзывы
	          </router-link>
			  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
			    <span class="navbar-toggler-icon"></span>
			  </button>

			  <div class="collapse navbar-collapse" id="navbarSupportedContent">
			    <ul class="navbar-nav mr-auto">

	 	       	  <router-link to="/stat" class="nav-link" exact-active-class="active">
	                Анализ
	              </router-link>
	              <router-link to="/trends" class="nav-link" active-class="active">
	                Тренды
	              </router-link> 
	              <router-link to="/dashboard" class="nav-link" active-class="active">
	                Обзор
	              </router-link> 
	              <router-link to="/" class="nav-link" exact-active-class="active">
	                Тест
	              </router-link> 

			    </ul>
			    <ul class="navbar-nav">
			      <router-link to="/teams" class="nav-link" active-class="active">
	                Команды
	              </router-link>
			    </ul>
			  </div>
			</div>
		</nav>
	</div>
</template>
