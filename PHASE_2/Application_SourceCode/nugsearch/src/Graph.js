import React from 'react'
import './Graph.css'
import { ResponsiveLine } from '@nivo/line'

import graphImage from './Graph.PNG'
import { withRouter } from 'react-router-dom';


class Graph extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            data: [
                {
                  "id": "japan",
                  "color": "hsl(130, 70%, 50%)",
                  "data": [
                    {
                      "x": "plane",
                      "y": 115
                    },
                    {
                      "x": "helicopter",
                      "y": 160
                    },
                    {
                      "x": "boat",
                      "y": 264
                    },
                    {
                      "x": "train",
                      "y": 21
                    },
                    {
                      "x": "subway",
                      "y": 213
                    },
                    {
                      "x": "bus",
                      "y": 110
                    },
                    {
                      "x": "car",
                      "y": 85
                    },
                    {
                      "x": "moto",
                      "y": 144
                    },
                    {
                      "x": "bicycle",
                      "y": 154
                    },
                    {
                      "x": "horse",
                      "y": 295
                    },
                    {
                      "x": "skateboard",
                      "y": 230
                    },
                    {
                      "x": "others",
                      "y": 62
                    }
                  ]
                },
                {
                  "id": "france",
                  "color": "hsl(26, 70%, 50%)",
                  "data": [
                    {
                      "x": "plane",
                      "y": 118
                    },
                    {
                      "x": "helicopter",
                      "y": 76
                    },
                    {
                      "x": "boat",
                      "y": 54
                    },
                    {
                      "x": "train",
                      "y": 7
                    },
                    {
                      "x": "subway",
                      "y": 201
                    },
                    {
                      "x": "bus",
                      "y": 63
                    },
                    {
                      "x": "car",
                      "y": 59
                    },
                    {
                      "x": "moto",
                      "y": 241
                    },
                    {
                      "x": "bicycle",
                      "y": 278
                    },
                    {
                      "x": "horse",
                      "y": 118
                    },
                    {
                      "x": "skateboard",
                      "y": 37
                    },
                    {
                      "x": "others",
                      "y": 190
                    }
                  ]
                },
                {
                  "id": "us",
                  "color": "hsl(238, 70%, 50%)",
                  "data": [
                    {
                      "x": "plane",
                      "y": 97
                    },
                    {
                      "x": "helicopter",
                      "y": 170
                    },
                    {
                      "x": "boat",
                      "y": 4
                    },
                    {
                      "x": "train",
                      "y": 135
                    },
                    {
                      "x": "subway",
                      "y": 166
                    },
                    {
                      "x": "bus",
                      "y": 142
                    },
                    {
                      "x": "car",
                      "y": 240
                    },
                    {
                      "x": "moto",
                      "y": 159
                    },
                    {
                      "x": "bicycle",
                      "y": 296
                    },
                    {
                      "x": "horse",
                      "y": 83
                    },
                    {
                      "x": "skateboard",
                      "y": 206
                    },
                    {
                      "x": "others",
                      "y": 279
                    }
                  ]
                },
                {
                  "id": "germany",
                  "color": "hsl(203, 70%, 50%)",
                  "data": [
                    {
                      "x": "plane",
                      "y": 261
                    },
                    {
                      "x": "helicopter",
                      "y": 286
                    },
                    {
                      "x": "boat",
                      "y": 221
                    },
                    {
                      "x": "train",
                      "y": 206
                    },
                    {
                      "x": "subway",
                      "y": 280
                    },
                    {
                      "x": "bus",
                      "y": 220
                    },
                    {
                      "x": "car",
                      "y": 212
                    },
                    {
                      "x": "moto",
                      "y": 23
                    },
                    {
                      "x": "bicycle",
                      "y": 31
                    },
                    {
                      "x": "horse",
                      "y": 274
                    },
                    {
                      "x": "skateboard",
                      "y": 147
                    },
                    {
                      "x": "others",
                      "y": 215
                    }
                  ]
                },
                {
                  "id": "norway",
                  "color": "hsl(355, 70%, 50%)",
                  "data": [
                    {
                      "x": "plane",
                      "y": 48
                    },
                    {
                      "x": "helicopter",
                      "y": 151
                    },
                    {
                      "x": "boat",
                      "y": 159
                    },
                    {
                      "x": "train",
                      "y": 223
                    },
                    {
                      "x": "subway",
                      "y": 131
                    },
                    {
                      "x": "bus",
                      "y": 169
                    },
                    {
                      "x": "car",
                      "y": 107
                    },
                    {
                      "x": "moto",
                      "y": 30
                    },
                    {
                      "x": "bicycle",
                      "y": 128
                    },
                    {
                      "x": "horse",
                      "y": 135
                    },
                    {
                      "x": "skateboard",
                      "y": 194
                    },
                    {
                      "x": "others",
                      "y": 129
                    }
                  ]
                }
              ]
        }
    }

    render() {
        return(
        <div>
            <div className="ResultBackground">
                <h2>Graph: COVID19 Results in World Between 01/01/2021 and 01/04/2021</h2>
                {/* <img src={graphImage} alt="img" class="GraphImage"/> */}
                <ResponsiveLine
                    data={this.state.data}
                    margin={{ top: 50, right: 110, bottom: 100, left: 60 }}
                    xScale={{ type: 'point' }}
                    yScale={{ type: 'linear', min: 'auto', max: 'auto', stacked: true, reverse: false }}
                    axisTop={null}
                    axisRight={null}
                    axisBottom={{
                        orient: 'bottom',
                        tickSize: 5,
                        tickPadding: 5,
                        tickRotation: 0,
                        legend: 'transportation',
                        legendOffset: 36,
                        legendPosition: 'middle'
                    }}
                    axisLeft={{
                        orient: 'left',
                        tickSize: 5,
                        tickPadding: 5,
                        tickRotation: 0,
                        legend: 'count',
                        legendOffset: -40,
                        legendPosition: 'middle',
                        fontColor: 'white',
                    }}
                    pointSize={10}
                    pointColor={{ theme: 'background' }}
                    pointBorderWidth={2}
                    pointBorderColor={{ from: 'serieColor' }}
                    pointLabelYOffset={-12}
                    useMesh={true}
                    legends={[
                        {
                            anchor: 'bottom-right',
                            direction: 'column',
                            justify: false,
                            translateX: 100,
                            translateY: 0,
                            itemsSpacing: 0,
                            itemDirection: 'left-to-right',
                            itemWidth: 80,
                            itemHeight: 20,
                            itemOpacity: 0.75,
                            symbolSize: 12,
                            symbolShape: 'circle',
                            symbolBorderColor: 'rgba(0, 0, 0, .5)',
                            effects: [
                                {
                                    on: 'hover',
                                    style: {
                                        itemBackground: 'rgba(0, 0, 0, .03)',
                                        itemOpacity: 1
                                    }
                                }
                            ]
                        }
                    ]}
                    theme={theme}
                />
                <p />
                <a href="/map">See Map</a>
            </div>
        </div>
        )
    }
}

export default withRouter(Graph);

const theme = {
    axis: {
        fontSize: "14px",
        tickColor: "#eee",
        ticks: {
            line: {
                stroke: "#555555"
            },
            text: {
                fill: "#ffffff"
            }
        },
        legend: {
            text: {
                fill: "#ffffff"
            }
        }
    }
}