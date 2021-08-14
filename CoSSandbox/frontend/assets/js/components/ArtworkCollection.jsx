import React, { Component } from 'react';

class ArtworkCollection extends Component {
    constructor(props) {
        super(props);
        this.state = {
            activeArtwork: null,
        };
    }
    render() { 
        return (
            <div>
                <h1>
                    {this.props.collection.collection_name}
                </h1>
            </div>
        );
    }
}
 
export default ArtworkCollection;
