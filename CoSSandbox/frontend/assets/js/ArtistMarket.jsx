import React, { Component } from 'react';
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
} from 'react-router-dom';

import CollectionList from "./components/CollectionList";

class ArtistMarket extends Component {
    constructor(props) {
        super(props);
        this.state = {
            collections: [],
            artworks: [],
        }

        this.viewCollection = this.viewCollection.bind(this);
    }

    componentDidMount() {
        this.fetchCollections();
    }

    componentDidUpdate(prevProps, prevState) {
        if (prevState.artworks != this.state.artworks && this.state.artworks.length > 0) {
            console.log('artworks updated');
        }
    }

    async fetchCollections() {
        const url = new URL("/collections", "http://127.0.0.1:8000");
        url.searchParams.append('format', 'json');

        const params = {
            method: 'GET',
            header: {
                'Content-type': 'application/json',
            },
        }

        try {
            const res = await fetch(url.toString(), params);
    
            if (!res.ok) {
                const message = `An error has occured: ${res.status}`;
                throw new Error(message);
            }
    
            const collections = await res.json();
    
            this.setState({
                collections,
            });
        } catch (e) {
            console.log(e);
        }
    }

    async fetchArtworks(id) {
        const url = new URL(`/artworks/${id}`, "http://127.0.0.1:8000");
        url.searchParams.append('format', 'json');

        const params = {
            method: 'GET',
            header: {
                'Content-type': 'application/json',
            },
        }

        try {
            const res = await fetch(url.toString(), params);
    
            if (!res.ok) {
                const message = `An error has occured: ${res.status}`;
                throw new Error(message);
            }
    
            const artworks = await res.json();
    
            this.setState({
                artworks,
            });
        } catch (e) {
            console.log(e);
        }
    }

    viewCollection(e) {
        e.preventDefault();

        const id = e.target.parentElement.id;
        this.fetchArtworks(id);
    }
    
    render() { 
        return (
            <Router>
                <CollectionList 
                    collections={this.state.collections}
                    viewCollection={this.viewCollection}
                />
            </Router>
        );
    }
}
 
export default ArtistMarket;
