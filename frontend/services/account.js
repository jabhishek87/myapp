angular.module('MyApp')
  .factory('Account', function($http) {
    return {
      getProfile: function() {
        return $http.get('/api/profile/me/');
      },
      updateProfile: function(profileData) {
        return $http.put('/api/profile/me/', profileData);
      }
    };
  });