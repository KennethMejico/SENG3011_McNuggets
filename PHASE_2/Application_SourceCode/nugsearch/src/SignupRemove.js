import React from 'react'
import './Signup.css'
import { withRouter } from 'react-router-dom';

class SignupRemove extends React.Component {
    constructor(props) {
        super(props);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleSubmit(event) {
        event.preventDefault();
        this.props.history.push({
            pathname: '/signup',
        });
    }

    render() {
      return (
        <div className="SignupApp">
            <h1>See you around</h1>
            <p>You've been taken off our Alert mailing list</p>
            <p>We won't contact you any further</p>
            <form onSubmit={this.handleSubmit}>
                <input type="submit" onSubmit={this.handleSubmit} className="longerSubmit" value="Rejoin the mailing list"/>
            </form>
        </div>
      );
    }
}

export default withRouter(SignupRemove);