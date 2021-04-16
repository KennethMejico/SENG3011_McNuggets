import React from 'react';
import './AlertBadges.css'
import { withRouter } from 'react-router-dom';

class AlertBadges extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            alerts: []
        };
    }

    componentDidMount() {
        alert = this.props.match.params.alert;
        this.getAlerts(alert);
    }

    getAlerts(alert) {
        fetch('/getAlerts').then(res => res.json()).then(data => {
            var index = data.alerts.indexOf(alert);
            if (index !== -1) {
                data.alerts.splice(index, 1);
            }
            this.setState({alerts: data.alerts});
        })
    }

    componentWillReceiveProps(nextProps) {
        this.getAlerts(nextProps.match.params.alert);
    }

    navigateToPage = (event) => {
        this.props.history.push('/alerts/' + event.target.dataset.alertname);
        this.setState({alerts: []});
    }

    AlertBadge(alert) {
        return (
            <div className="AlertBadge" key={alert} data-alertname={alert} onClick={this.navigateToPage}>
                OUTBREAK OF {alert.toUpperCase()} COULD LEAD TO LOCKDOWN
            </div>
        );
    }

    render() {
        return (
            <div className="AlertBadgeArea">
                {Object.keys(this.state.alerts).map((alert) => (
                    this.AlertBadge(this.state.alerts[alert])
                ))}
            </div>
        )
    }
}

export default withRouter(AlertBadges);