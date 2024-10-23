from flaskavel.lab.beaker.routes.router import Route

Route.middleware(['csrf']).prefix('v1').controller('HomeController').group(
    Route.get("/test/{id}", "index").name("user.index"),
)