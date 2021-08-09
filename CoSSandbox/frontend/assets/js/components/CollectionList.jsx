import React, { Component } from 'react';

class CollectionList extends Component {
    constructor(props) {
        super(props);
        this.state = {
            collections: [],
        }
    }
    render() { 
        return (
            <div className="collection-list">
                <h1>Wello Horld!</h1>
            </div>
        );
    }
}
 
export default CollectionList;
