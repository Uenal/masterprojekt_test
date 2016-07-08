var React = require('react')
  , request = require('superagent');

var DeleteSensor = React.createClass({

  propTypes: {
    cancleCallback: React.PropTypes.func,
    sensor: React.PropTypes.object
  },

  getInitialState: function() {
    return {
    };
  },

  handleSaveClick: function(){
    request.delete('/sensor/' + this.props.sensor.id)
      .end(function(err, res) {
        if (err) return console.log(err);
        if (res.statusCode === 200) {
          window.location.pathname = '/sensors';
        }
      });
  },

  render: function() {
    return (
      <div className='iot-modal callout'>
        <h2 id='modalTitle'>Delete Sensor: {this.props.sensor.name} ?</h2>
        <div className="body">
          <div className='row columns' style={{marginTop: 25, textAlign: 'right'}}>
            <div className='small-12 column'>
              <div className='button alert' onClick={this.props.cancleCallback}>no</div>
              <div className='button' onClick={this.handleSaveClick}>yes</div></div>
          </div>
        </div>
      </div>
    );
  }

});

module.exports = DeleteSensor;
