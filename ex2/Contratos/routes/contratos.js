var express = require('express');
var router = express.Router();
var axios = require('axios');

/* GET users listing. */
router.get('/', function(req, res, next) {
  var d = new Date().toISOString().substring(0,16)
  axios.get("http://localhost:3000/Contratos?_sort=id")
    .then(resp =>{
      contratos = resp.data
      res.status(200).render("contratosListPage", {"lContratos" : contratos, "date" : d})
    })
    .catch(erro =>{
      res.status(501).render("error", {"error" : erro})
    })
});

router.get('/:id', function(req, res, next) {
  var d = new Date().toISOString().substring(0,16)
  var id = req.params.id
  axios.get("http://localhost:3000/Contratos/" + id)
    .then(resp =>{
      var contrato = resp.data
      res.status(200).render("contratoPage", {"contrato" : contrato, "date" : d})
    })
    .catch(erro =>{
      res.status(502).render("error", {"error" : erro})
    })
});

router.get('/entidades/:nipc', function(req, res, next) {
  var d = new Date().toISOString().substring(0,16)
  var nipc = req.params.nipc
  axios.get("http://localhost:3000/Entidades?nipc=" + nipc)
  .then(resp =>{
    var entidade = resp.data
    //console.log(entidade)
      res.status(200).render("entidadePage", {"entidade" : entidade, log: console.log, "date" : d})
    })
    .catch(erro =>{
      res.status(503).render("error", {"error" : erro})
    })
});


module.exports = router;