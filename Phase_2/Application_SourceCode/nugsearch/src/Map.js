import React from 'react'
import './Map.css'

import mapImage from './Map.PNG'
import { withRouter, Link } from 'react-router-dom';
import GOOGLE_MAP_API_KEY from './GOOGLE_MAP_API_KEY.js';


class Map extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            googleMap: null
        };
        console.log(props);
    }

    componentDidMount() {
        const googleMapScript = document.createElement('script');
        googleMapScript.src = `https://maps.googleapis.com/maps/api/js?key=${GOOGLE_MAP_API_KEY}&libraries=places`;
        window.document.body.appendChild(googleMapScript);

        googleMapScript.addEventListener('load', () => {
            this.setState({googleMap: this.createMap()})
            this.placeMarkersAndBounds(this.fetchData(this.props.date, this.props.location))
        });
    }

    render() {
        return(
            <div>
                <div className="ResultBackground">
                    <h2>Map: COVID19 Results in World Between {this.props.location.state.startDate} and {this.props.location.state.endDate}</h2>
                    <div id="map" className="mapClass" > <img src={mapImage} alt="img" className="ResultImage"/> </div>
                    <p />
                    <Link to={{
                        pathname: '/graph',
                        state: {
                            data: this.props.location.state.data,
                            startDate: this.props.location.state.startDate,
                            endDate: this.props.location.state.endDate,
                        }
                    }}>See Graph</Link>
                </div>
            </div>
        )
    }

    createMap = () =>
        new window.google.maps.Map(document.getElementById('map'), {
            zoom: 9,
            center: {lat: -33.7688, lng: -208.8593},
            mapTypeId: 'terrain',
            disableDefaultUI: true
        })

    fetchData(date, location){
        fetch('getMap?date='+date+'&location='+location)
        .then(res => res.json())
        .then(data => {
            return data;
        });
    }

    placeMarkersAndBounds(data){

    }

}

export default withRouter(Map);
