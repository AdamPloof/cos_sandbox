import React, { Component } from 'react';

class Artwork extends Component {
    render() {
        const { artist, created_date, description, image, title, published_date } = this.props.artwork;
        const webRoot = "http://127.0.0.1:8000";
        const imageUrl = webRoot + image;

        return (
            <div className="artwork-card">
                <div className="card-header">
                    <div className="header-left">
                        {title}
                    </div>
                    <div className="header-right">
                        {artist}
                    </div>
                </div>
                <div className="card-sub-header">
                    <div className="header-left">
                        Created: {created_date}
                    </div>
                    <div className="header-right">
                        Published: {published_date}
                    </div>
                </div>
                <div className="card-body">
                    <div className="image-wrapper">
                        <img src={imageUrl} alt="ArtworkImage" />
                    </div>
                    <div className="artwork-text-box">
                        <p>{description}</p>
                    </div>
                </div>
            </div>
        );
    }
}
 
export default Artwork;
