import ReactDOM from 'react-dom';

// JS
import CollectionList from "./components/CollectionList";

// SCSS
import '../scss/app.scss';

const initApp = () => {
    console.log('Wello Horld!');
    ReactDOM.render(document.body, <CollectionList />);
}

initApp();
