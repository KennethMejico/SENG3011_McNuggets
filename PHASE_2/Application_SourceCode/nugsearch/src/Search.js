import React from 'react';
import './Search.css'

class Search extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            value: ''
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({value: event.target.value});
    }

    handleSubmit(event) {
        alert('A name was submitted: ' + this.state.value);
        event.preventDefault();
    }

    getSubparts = () => {

    }

    render() {
      return (
        <div>
            <KeywordForm />
            <p />
            <LocationForm />
            <p />
            <DateForm />
            <p />
            <form onSubmit={this.getSubparts}>
                <input type="submit" value="Submit"/>
            </form>
        </div>
      );
    }
}

class KeywordForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            value: ''
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({value: event.target.value});
    }

    handleSubmit(event) {
        alert(this.state.value + "was entered");
        event.preventDefault();
    }

    render() {
      return (
        <form>
            <label>
                <input type="text" value={this.state.value} onChange={this.handleChange} className="KeywordText" placeholder="Search for keywords"/>
            </label>
        </form>
      );
    }
}

class LocationForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            value: ''
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({value: event.target.value});
    }

    handleSubmit(event) {
        alert(this.state.value + "was entered");
        event.preventDefault();
    }

    setDefaultLocation = () => {
        fetch('/currentLocation')
        .then(res => res.json())
        .then(data => {
            this.setState({value: data.location})
        });
    }

    render() {
      return (
        <div className="Location">
            <form>
                <label>
                    Location:
                </label>
                <input type="text" value={this.state.value} onChange={this.handleChange} className="LocationText" placeholder="Choose a location"/>
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
        this.state = {
            value: ''
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({value: event.target.value});
    }

    handleSubmit(event) {
        alert(this.state.value + "was entered");
        event.preventDefault();
    }

    render() {
      return (
        <div className="Date">
            <form>
                <label>
                    Date Range:
                </label>
                <input type="text" value={this.state.value} onChange={this.handleChange} className="DateText" placeholder="yyyy-mm-ddThh:mm:ss"/>
            </form>
            <form>
                <label>
                    -
                </label>
                <input type="text" value={this.state.value} onChange={this.handleChange} className="DateText" placeholder="yyyy-mm-ddThh:mm:ss"/>
            </form>
        </div>
      );
    }
}

export default Search;