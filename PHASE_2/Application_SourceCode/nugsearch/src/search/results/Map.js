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
    }

    componentDidMount() {
        const googleMapScript = document.createElement('script');
        googleMapScript.src = `https://maps.googleapis.com/maps/api/js?key=${GOOGLE_MAP_API_KEY}&libraries=places`;
        window.document.body.appendChild(googleMapScript);

        googleMapScript.addEventListener('load', () => {
            this.setState({googleMap: this.createMap()});
            fetch('getMap?date='+this.props.date+'&location='+this.props.ulocation).then(res => res.json()).then(data => {
                console.log(this.props.ulocation);
                this.placeMarkersAndBounds(data);
            });
        });
    }

    render() {
        if (typeof this.props.location === 'undefined' || typeof this.props.location.state === 'undefined'){
            return(
                <div>
                    <div className="ResultBackground">
                        <div id="map" className="mapClass" > <img src={mapImage} alt="img" className="ResultImage"/> </div>
                    </div>
                </div>
            )
        } else {
            return(
                <div>
                    <div className="ResultBackground">
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
    }

    createMap = () =>
        new window.google.maps.Map(document.getElementById('map'), {
            zoom: 9,
            center: {lat: -33.7688, lng: -208.8593},
            mapTypeId: 'terrain',
            disableDefaultUI: true
        })

    placeMarkersAndBounds(data){
        // Unpack data
        var regions = data.regions;
        var caseLocations = data.caseLocations;
        // Temp Reference to Map. 
        var gmap = this.state.googleMap;
        // Set center to requested location
        gmap.setCenter(new window.google.maps.LatLng(data.center));
        // Colours based on how bad things be. Using array so can update colours later.
        var colourArray = ["#00FF00","#85d700","#e59100","#e15300","#FF0000"]
        // For item in regions:
        // Highlight the region in a colour symbolizing how likely we think lockdown is.
        var i;
        for (i=0; i < regions.length; i++){
            var probLevel = this.convert(
                regions[i].probabilityOfLockdown, [0, colourArray.length-1]
            );
            var mbounds = new window.google.maps.LatLngBounds(
                new window.google.maps.LatLng(regions[i].regionBounds.southwest),   //SW
                new window.google.maps.LatLng(regions[i].regionBounds.northeast)    //NE
            );
            new window.google.maps.Rectangle({
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
        for (i=0; i < caseLocations.length; i++){
            new window.google.maps.Marker({
                position: new window.google.maps.LatLng(caseLocations[i].location),
                label: caseLocations[i].caseCount,
                map: gmap
            });
        }

        console.log("Done");
    }

    // Converts number from 0 to 100 to another range
    convert = (number, range) => (((number * (range[1] - range[0])) / 100) + range[0])

}

export default withRouter(Map);