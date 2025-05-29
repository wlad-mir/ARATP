# ARATP
<h1> Automation of REST API testing in Python </h1>

<a target="_blank" href="https://playground.learnqa.ru/api/map/">LearnQA API</a>



<!-- Technologies used in the project -->

<h2> Technologies used in the project</h2>
<p  align="center">
  <code><img width="5%" title="Python" src="icons/python.png"></code>
  <code><img width="5%" title="Github" src="icons/github.png"></code>
  <code><img width="5%" title="Pytest" src="icons/pytest.png"></code>
  <code><img width="5%" title="Requests" src="icons/requests.png"></code>
  <code><img width="5%" title="PyCharm" src="icons/pycharm.png"></code>
  <code><img width="5%" title="VS Code" src="icons/vscode.png"></code>
  <code><img width="5%" title="Allure Report" src="icons/allure.png"></code>
  <code><img width="5%" title="Docker" src="icons/docker.png"></code>
  <code><img width="5%" title="Docker Compose" src="icons/docker-compose.png"></code>
  <code><img width="5%" title="Faker" src="icons/faker.png"></code>
</p>


<!-- Test cases -->

<h2>Automation of API methods depending on HTTP request type:</h2>

* ✅ Create user
* ✅ Logs user into the system
* ✅ Get user id you are authorizes as OR get 0 if not authorized
* ✅ Get user info by id
* ✅ Update user
* ✅ Delete user by id


<!-- Docker -->

<h2>Creating a project image in Docker</h2>
docker build -t pytest_runner

### Running tests from a project image in Docker
docker run --rm --mount type=bind,src="project_folder",target=/tests_project/ pytest_runner

<!-- Docker Compose -->

<h2>Creating a project image in Docker Compose</h2>
docker-compose build

### Running tests from a project image in Docker Compose
docker-compose up


<!-- Allure report -->

<h2> Allure report </h2>

<p  align="center">
  <code><img title="Overview" src="images/overview.png"></code>

  <code><img title="Suites" src="images/suites.png"></code>

  <code><img title="Graphs" src="images/graphs.png"></code>

  <code><img title="Behaviors" src="images/behaviors.png"></code>

  <code><img title="Packages" src="images/packages.png"></code>
</p>
