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
        // Unpack data
        regions = data.regions;
        caseLocations = data.caseLocations;
        // Temp Reference to Map. 
        gmap = this.state.googleMap;
        // Set center to requested location
        gmap.setCenter(new google.maps.LatLng(data.center));
        // Colours based on how bad things be. Using array so can update colours later.
        colourArray = ["#00FF00","#85d700","#e59100","#e15300","#FF0000"]
        // For item in regions:
        // Highlight the region in a colour symbolizing how likely we think lockdown is.
        for (var i=0; i < regions.length; i++){
            var probLevel = this.convert(
                regions[i].probabilityOfLockdown, [0, colourArray.length-1]
            );
            var mbounds = new google.maps.LatLngBounds(
                new google.maps.LatLng(regions[i].regionBounds.southWest),   //SW
                new google.maps.LatLng(regions[i].regionBounds.northEast)    //NE
            );
            new google.maps.Rectangle({
                strokeColor: colourArray[probLevel],
                fillColor: colourArray[probLevel],
                strokeOpacity: 0.35,
                fillOpacity: 0.35,
                strokeWeight: 1,
                map: gmap,
                bounds: mbounds
            })
        }
        // For item in case locations:
        // Place a marker with how many cases were there.
        for (var i=0; i < caseLocations.length; i++){
            new google.maps.Marker({
                position: new google.maps.LatLng(caseLocations[i].location),
                label: caseLocations[i].caseCount,
                map: gmap
            });
        }
    }

    // Converts number from 0 to 100 to another range
    convert = (number, range) => (((number * (range[1] - range[0])) / 100) + range[0])

}

export default withRouter(Map);
