import React from 'react'
import './Signup.css'
import { withRouter } from 'react-router-dom';

class SignupFinish extends React.Component {
    constructor(props) {
        super(props);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleSubmit(event) {
        event.preventDefault();
        this.props.history.push({
            pathname: '/signupRemove',
        });
    }

    render() {
      return (
        <div className="SignupApp">
            <h1>Thanks for signing up</h1>
            <p>You should shortly recieve an email confirming you want to receive alerts</p>
            <p>If no email arrives, double check that you entered the right email</p>
            <p>From now on, we will not contact your email for anything except alerts</p>
            <form onSubmit={this.handleSubmit}>
                <input type="submit" onSubmit={this.handleSubmit} value="Wait, take me off the list"/>
            </form>
        </div>
      );
    }
}

export default withRouter(SignupFinish);