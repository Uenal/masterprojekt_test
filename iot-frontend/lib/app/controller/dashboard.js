var React = require('react')
  , ReactDOM = require('react-dom/server')
  , Dashboard = React.createFactory(
      require('../../public/react/Dashboard')
    );

module.exports = me = {};

me.render = function(req, res) {
  var out = {
      user: {
        firstname: req.user.firstname,
        username: req.user.username,
        isAdmin: req.isAdmin
      },
    sensors: req.sensors || [],
    gateways: req.gateways || [],
    clusters: req.clusters || []
  };
  var dashboard = new Dashboard(out);
  var body = ReactDOM.renderToString(dashboard);

  res.render('dashboard', {body: body, reactData: out});
};
