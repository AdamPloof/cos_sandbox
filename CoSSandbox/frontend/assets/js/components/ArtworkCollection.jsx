import React, { Component } from 'react';

class ArtworkCollection extends Component {
    constructor(props) {
        super(props);
        this.state = {
            activeArtwork: null,
        };

        this.viewArtwork = this.viewArtwork.bind(this);
    }

    componentDidMount() {
        this.props.fetchArtworks(this.props.collection.id);
    }

    componentDidUpdate(prevProps, prevState) {
        if (this.props.collection != prevProps.collection) {
            this.props.fetchArtworks();
        }
    }

    viewArtwork(e) {
        let { history } = this.props.routeProps;
        history.push(`/artwork/${e.target.id}`);
    }

    makeArtworkGrid() {
        let artworks = [...this.props.artworks];
        let mosaics = [];
        let artworkBatch = [];
        while (artworks.length > 6) {
            artworkBatch = artworks.splice(0, 6);
            mosaics.push(this.makeMosaic(artworkBatch));
            artworkBatch = []; // probably can skip this step but, just to be safe, let's empty the batch at the end of each loop
        }

        // Make one more partial mosaic with any remaining artworks
        if (artworks.length > 0) {
            mosaics.push(this.makeMosaic(artworks));
        }

        return (
            <div className="artwork-grid">
                {mosaics.map((mosaic) => mosaic)}
            </div>
        );
    }

    makeMosaic(artworkBatch) {
        // It is assumed that the length of artworkBatch will always be <= 6
        let mosaicSizes = [
            'medium',
            'large',
            'medium-tall',
            'small',
            'tall',
            'wide',
        ];

        // In order to give the mosaic-container a unique key, we'll use the id of the first artwork in the batch
        return (
            <div key={artworkBatch[0].id} className="mosaic-container">
                {artworkBatch.map(artwork => {
                    return this.makeMosaicItem(artwork, mosaicSizes.shift());
                })}
            </div>
        );
    }

    makeMosaicItem(artwork, size) {
        const webRoot = "http://127.0.0.1:8000";
        const imageUrl = webRoot + artwork.image;
        return (
            <div 
                key={artwork.id}
                id={artwork.id}
                className={`mosaic-item ${size}`} 
                style={{"backgroundImage": `url(${imageUrl})`}}
                onClick={this.viewArtwork}
            >
                {artwork.title}
            </div>
        );
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
                    {this.makeArtworkGrid()}
                </div>
            </div>
        );
    }
}
 
export default ArtworkCollection;
