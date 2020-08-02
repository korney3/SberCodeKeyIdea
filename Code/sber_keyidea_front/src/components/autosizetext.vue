<template>
    <textarea type="text" 
    	v-model="value" 
    	@input="$emit('input', value)"
    	rows="3" 
    	ref="textarea_elem"
    	@keyup="updateHeight" @focus="updateHeight"></textarea>
</template>

<script>
    export default {
        name: 'longtext',
        props:['value', 'record'],
        data() {
        	return {
        		height: '20px',
        	}
        },
        mounted(){
	        this.updateHeight();
	    },
        computed: {
        	text() {
        		return this.value;
        	},
        },
        watch: {
        	text() {
        		this.updateHeight()
        		setTimeout(this.updateHeight, 1)
        	}
        },
        methods: {
        	updateHeight() {
				this.$refs.textarea_elem.style.height = "20px";
        		this.$refs.textarea_elem.style.height = (this.$refs.textarea_elem.scrollHeight+10) + "px";
        	},
        }
    }
</script>