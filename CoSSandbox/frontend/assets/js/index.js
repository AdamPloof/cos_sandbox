// JS
import "core-js/stable";
import "regenerator-runtime/runtime";

import React from 'react';
import ReactDOM from 'react-dom';

import ArtistMarket from './ArtistMarket';

// SCSS
import bootstrap from 'bootstrap';
import '../scss/app.scss';

const initApp = () => {
    console.log('Wello Horld!');
    ReactDOM.render(<ArtistMarket />, document.getElementById('collection-list'));
}

initApp();
