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
    ReactDOM.render(<ArtistMarket />, document.getElementById('collection-app'));
}

initApp();
