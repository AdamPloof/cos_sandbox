import React, { Component } from 'react';
import { Link } from 'react-router-dom';

class Artwork extends Component {
    constructor(props) {
        super(props);
        this.handleClick = this.handleClick.bind(this);
    }

    handleClick(e) {
        e.preventDefault();
        let { history } = this.props.routeProps;
        history.goBack();
    }

    render() {
        const { artist, created_date, description, image, title, published_date } = this.props.artwork;
        const webRoot = "http://127.0.0.1:8000";
        const imageUrl = webRoot + image;
        const imgWidth = "700px";

        return (
            <div className="card" style={{width: imgWidth, margin: "2rem auto 5rem auto"}}>
                <div className="card-header" style={{display: "flex", flexDirection: "row", justifyContent: "flex-end"}}>
                    <a href="#" onClick={this.handleClick}>Back to Collection</a>
                </div>
                <img src={imageUrl} className="card-img-top" alt="ArtworkImage" style={{width: imgWidth}}  />
                <div className="card-body">
                    <div className="card-title">
                        <div className="title-left">
                            <h5>{title}</h5>
                        </div>
                        <div className="title-right">
                            <small className="text-muted">
                                {artist}
                            </small>
                        </div>
                    </div>
                    <p className="card-text">
                        {description}
                    </p>
                </div>
                <div className="card-footer" style={{display: "flex", flexDirection:"row", justifyContent: "space-between"}}>
                    <div className="footer-left">
                        <strong>Created:</strong><span className="text-muted">&nbsp;{created_date}</span>
                    </div>
                    <div className="footer-right">
                        <strong>Published:</strong><span className="text-muted">&nbsp;{published_date}</span>
                    </div>
                </div>
            </div>
        );
    }
}
 
export default Artwork;
