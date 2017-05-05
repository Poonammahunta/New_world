(function () {
  
  var app;
  app = angular.module('caseLister',[]);
  
  app.controller('listController', ['$http', '$scope', function($http, $scope){
    
    
	this.server_url = 'https://roles-directory.apps-test.valeo.com/role_export_through_url/download';
    this.credentials = {
         grant_type   : 'password',
         scope        : '*',
         username     : '',
         password     : ''
    };
	 
	 var access_token = '';	 
	 var list = this;
	 
    this.login = function () {
		 var parameters = {
			 method: 'POST',
			 url: list.server_url+list.workspace+'/oauth2/token',
			 data: this.credentials
	    };
		 $http(parameters).success(function(data){
		 	if (data.error) {
		 		alert(data.error_description);
		 	}else {
		 		parameters = {
					 method: 'GET',
					 url: list.server_url+'api/1.0/'+list.workspace+',
					 headers: {'Authorization': 'Bearer '+data.access_token}
			    };
				$http(parameters).success(function(data){
				
				  list.cases = data;
				  var str = JSON.stringify(data);
				 // list.cases = str;
				  alert(str);
				  
				});
			  
			}
		 });
	 };
	 	 
  }]);
  
})();