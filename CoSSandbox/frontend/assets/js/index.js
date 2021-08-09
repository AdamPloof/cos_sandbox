import ReactDOM from 'react-dom';

import CollectionList from "./components/CollectionList";

const initApp = () => {
    console.log('Wello Horld!');
    ReactDOM.render(document.body, <CollectionList />);
}

initApp();
