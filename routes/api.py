from flaskavel.lab.beaker.routes.router import Route

Route.middleware(['csrf', 'api_key']).prefix('v1').controller('HomeController').group(
    Route.get("/user/{id}", "index").name("user.index"),
)