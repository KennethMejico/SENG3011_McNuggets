import React from 'react'
import './Signup.css'
import { withRouter } from 'react-router-dom';
import nugLogo from '../images/nugSearchLogo300.png';

class Signup extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            email: '',
            location: '',
        };
        this.changeEmail = this.changeEmail.bind(this);
        this.changeLocation = this.changeLocation.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    changeEmail(email) {
        this.setState({email: email})
    }

    changeLocation = (location) => {
        this.setState({location: location})
    }

    handleSubmit(event) {
        event.preventDefault();
        var re = /\S+@\S+\.\S+/;
        if (! re.test(this.state.email)) {
            alert("Please enter a valid email");
            return;
        }
        this.props.history.push({
            pathname: '/signupFinish',
        });
    }

    render() {
      return (
        <div className="SignupApp">
            <h1><img src={nugLogo} alt="logo" className="MediumLogo"/>Mailing List</h1>
            <p>Sign up to receive alerts on disease in your area</p>
            <p>If no location is provided, you will be sent alerts for everywhere in Australia</p>
            <p>We will not contact your email for anything except alerts and as part of the sign up process</p>
            <p>Your email will not be shared with anyone</p>
            <EmailForm onChange={this.changeEmail} email={this.state.email}/>
            <p />
            <LocationForm onChange={this.changeLocation} location={this.state.location}/>
            <p />
            <form onSubmit={this.handleSubmit}>
                <input type="submit" value="Submit"/>
            </form>
        </div>
      );
    }
}

class EmailForm extends React.Component {
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
                Email: 
            </label>
            <input type="text" value={this.props.keywords} onChange={this.handleChange} className="EmailText" placeholder="Please enter a valid email address to sign up"/>
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
                    temp.props.onChange(data.location)
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

export default withRouter(Signup);