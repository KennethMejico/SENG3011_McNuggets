import React from 'react';
import nugLogo from './nugSearchLogo300.png'
import './Search.css'
import { withRouter } from 'react-router-dom';

class Search extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            keywords: '',
            location: '',
            fromDate: '',
            toDate: ''
        };
        this.changeKeywords = this.changeKeywords.bind(this);
        this.changeLocation = this.changeLocation.bind(this);
        this.changeFromDate = this.changeFromDate.bind(this);
        this.changeToDate = this.changeToDate.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    changeKeywords(keywords) {
        this.setState({keywords: keywords})
    }

    changeLocation(location) {
        this.setState({location: location})
    }

    changeFromDate(fromDate) {
        this.setState({fromDate: fromDate})
    }

    changeToDate(toDate) {
        this.setState({toDate: toDate})
    }

    setLocation = (location) => {
        this.setState({
            location: location
        })
    }

    handleSubmit(event) {
        fetch('/search')
        .then(res => res.json())
        .then(data => {
            //alert("recieved: " + data.result)
        });
        event.preventDefault();
        this.props.history.push('/map');
    }

    render() {
      return (
        <div className="SearchApp">
            <h1><img src={nugLogo} alt="logo" className="MediumLogo"/>NugSearch</h1>
            <h2>Find the latest news about disease reports in your area</h2>
            <KeywordForm onChange={this.changeKeywords} keywords={this.state.keywords}/>
            <p />
            <LocationForm onChange={this.changeLocation} setLocation={this.setLocation} location={this.state.location}/>
            <p />
            <DateForm onFromChange={this.changeFromDate} onToChange={this.changeToDate}
                        fromDate={this.state.fromDate} toDate={this.state.toDate}/>
            <p />
            <form onSubmit={this.handleSubmit}>
                <input type="submit" value="Submit"/>
            </form>
        </div>
      );
    }
}

class KeywordForm extends React.Component {
    constructor(props) {
        super(props);
        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(event) {
        this.props.onChange(event.target.value);
    }

    render() {
      return (
        <form>
            <label>
                <input type="text" value={this.props.keywords} onChange={this.handleChange} className="KeywordText" placeholder="Search for keywords"/>
            </label>
        </form>
      );
    }
}

class LocationForm extends React.Component {
    constructor(props) {
        super(props);
        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(event) {
        this.props.onChange(event.target.value);
    }

    setDefaultLocation = () => {
        let temp = this;
        let latitude=null;
        let longitude=null;
        navigator.geolocation.getCurrentPosition(
            function(position) {
                latitude = position.coords.latitude;
                longitude = position.coords.longitude;
                console.log("Lat = "+ latitude + " &lon = " + longitude)
                fetch('/currentLocation?lat='+latitude+'&lon='+longitude)
                .then(res => res.json())
                .then(data => {
                    //console.log(data)
                    temp.props.setLocation(data.location)
                });
            },
            function(error) {
                console.error("Error Code = " + error.code + " - " + error.message);
                alert("User has disabled location");
                return;
            }
        );
    }

    render() {
      return (
        <div className="Location">
            <form>
                <label>
                    Location:
                </label>
                <input type="text" value={this.props.location} onChange={this.handleChange} className="LocationText" placeholder="Choose a location"/>
            </form>
            <form>
                <label>
                    or
                </label>
                <input type="button" value="Use my location" onClick={this.setDefaultLocation} className="LocationButton" placeholder="Search for keywords"/>
            </form>
        </div>
      );
    }
}

class DateForm extends React.Component {
    constructor(props) {
        super(props);
        this.handleFromChange = this.handleFromChange.bind(this);
        this.handleToChange = this.handleToChange.bind(this);
    }

    handleFromChange(event) {
        this.props.onFromChange(event.target.value);
    }

    handleToChange(event) {
        this.props.onToChange(event.target.value);
    }

    render() {
      return (
        <div className="Date">
            <form>
                <label>
                    Date Range:
                </label>
                <input type="text" value={this.props.fromDate} onChange={this.handleFromChange} className="DateText" placeholder="yyyy-mm-ddThh:mm:ss"/>
            </form>
            <form>
                <label>
                    -
                </label>
                <input type="text" value={this.props.toDate} onChange={this.handleToChange} className="DateText" placeholder="yyyy-mm-ddThh:mm:ss"/>
            </form>
        </div>
      );
    }
}

export default withRouter(Search);