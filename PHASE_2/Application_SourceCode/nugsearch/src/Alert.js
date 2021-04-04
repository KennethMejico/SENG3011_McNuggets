import React from 'react'
import './Alert.css'

import covidImg from './COVID-19-1080x515.jpg'
import alertImg from './Health-alert.png'

class Alert extends React.Component {
    render() {
        return(
            <div className="Background">
                <h1 className="Heading"> Alert: COVID19 Outbreak </h1>
                <img src={covidImg} alt="img" class="CovidImage"/>
                <p class="AlertText"> There were 17 cases of COVID-19 in Sydney on 10/04/2021.

In the past, this amount of cases has lead to a lockdown in your area. Be prepared for another to happen again.

COVID-19 has caused a lockdown in your area THREE times before. COVID-19 has caused lockdowns to happen way too many times in total.

The last COVID-19 lockdown happened after 15 cases were reported in a day.

See government alerts for your area: https://www.nsw.gov.au/
                </p>
                <div class="Divider"></div>
                <h2 className="OtherHeading"> Other Alerts </h2>
                <div class="row">
                    <div class="column">
                        <img src={alertImg} alt="alert1" class="Alert1" style={{ width: '80%' }}/>
                    </div>
                    <div class="column">
                        <img src={alertImg} alt="alert2" class="Alert2" style={{ width: '80%' }}/>
                    </div>
                    <div class="column">
                        <img src={alertImg} alt="alert3" class="Alert3" style={{ width: '80%' }}/>
                    </div>
                </div>
            </div>
        )
    }
}

export default Alert;