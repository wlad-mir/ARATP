# ARATP
<h1> Automation of REST API testing in Python </h1>

<a target="_blank" href="https://playground.learnqa.ru/api/map/">LearnQA API</a>



<!-- Technologies used in the project -->

### Technologies used in the project
<p  align="center">
  <code><img width="5%" title="Python" src="icons/python.png"></code>
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
Automation of API methods depending on HTTP request type:
* ✅ Create user
* ✅ Logs user into the system
* ✅ Get user id you are authorizes as OR get 0 if not authorized
* ✅ Get user info by id
* ✅ Update user
* ✅ Delete user by id


<!-- Docker -->

### <img width="3%" title="Docker" src="icon/docker.png"> Creating a project image in Docker
docker build -t pytest_runner

### Running tests from a project image in Docker
docker run --rm --mount type=bind,src="project_folder",target=/tests_project/ pytest_runner

<!-- Docker Compose -->

### <img width="3%" title="Docker Compose" src="icon/docker-compose.png"> Creating a project image in Docker Compose
docker-compose build

### Running tests from a project image in Docker Compose
docker-compose up


<!-- Allure report -->

### <img width="3%" title="Overview" src="images/overview.png"> Allure report

### <img width="3%" title="Suites" src="images/suites.png"> Allure report

### <img width="3%" title="Graphs" src="images/graphs.png"> Allure report

### <img width="3%" title="Behaviors" src="images/behaviors.png"> Allure report

### <img width="3%" title="Packages" src="images/packages.png"> Allure report

