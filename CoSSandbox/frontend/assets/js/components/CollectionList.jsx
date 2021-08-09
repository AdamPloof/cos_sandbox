import React, { Component } from 'react';

class CollectionList extends Component {
    makeCollectionList() {
        if (this.props.collections.lenght == 0) {
            return null;
        }

        return (
            <ul>
                {this.props.collections.map(collection => {
                    return (
                        <li key={collection.id} id={collection.id}>
                            <a href="#" onClick={this.props.viewCollection}>
                                {collection.collection_name}
                            </a>
                            <span>
                                - <small className="text-muted">{collection.collection_types}</small>
                            </span>
                        </li>
                    );
                })}
            </ul>
        );
    }

    render() { 
        return (
            <div className="list-container">
                <div className="container-header">
                    <h1>Collections</h1>
                </div>
                <div className="collection-list">
                    {this.makeCollectionList()}
                </div>
            </div>
        );
    }
}
 
export default CollectionList;
