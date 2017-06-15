/**
 * Created by michael on 14/06/17.
 */
/**
 * First we will load all of this project's JavaScript dependencies which
 * include Vue and Vue Resource. This gives a great starting point for
 * building robust, powerful web applications using Vue and Laravel.
 */

window.$ = window.jQuery = require('jquery');
require('bootstrap-sass');
import Vue from "vue";

import Demo from "./components/Demo.vue";

const app = new Vue({
    el: '#app',
    components: {
        Demo
    }
});