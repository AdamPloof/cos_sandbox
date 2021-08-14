import React, { Component } from 'react';

class ArtworkCollection extends Component {
    constructor(props) {
        super(props);
        this.state = {
            activeArtwork: null,
        };
    }

    componentDidMount() {
        this.props.fetchArtworks(this.props.collection.id);
    }

    componentDidUpdate(prevProps, prevState) {
        if (this.props.collection != prevProps.collection) {
            this.props.fetchArtworks();
        }
    }

    render() { 
        return (
            <div className="collection-container">
                <div className="container-header">
                    <h1>
                        {this.props.collection.collection_name}
                    </h1>
                </div>
                <div className="container-body">
                    <ul>
                        {this.props.artworks.map((artwork) => {
                            return (
                                <li key={artwork.id}>{artwork.title}</li>
                            );
                        })}
                    </ul>
                </div>
            </div>
        );
    }
}
 
export default ArtworkCollection;
