'use strict';

const React = require('react');
const ReactDOM = require('react-dom');
const client = require('./client');

const follow = require('./follow'); // function to hop multiple links by "rel"

const root = '/api';

class App extends React.Component {

	constructor(props) {
		super(props);
		this.state = {students: [], courses: [], attributes: [], links: {}};
		this.onCreate = this.onCreate.bind(this);
		this.onDelete = this.onDelete.bind(this);
	}

	loadFromServer() {
		follow(client, root, [
			{rel: 'students'}]
		).then(studentCollection => {
			return client({
				method: 'GET',
				path: studentCollection.entity._links.profile.href,
				headers: {'Accept': 'application/schema+json'}
			}).then(schema => {
				this.schema = schema.entity;
				return studentCollection;
			});
		}).then(studentCollection => {
			this.setState({
				students: studentCollection.entity._embedded.students,
				attributes: Object.keys(this.schema.properties),
				links: studentCollection.entity._links});
		}).then(client, root, [
			{rel: 'courses'}]
		).then(courseCollection => {
			return client({
				method: 'GET',
				path: courseCollection.entity._links.profile.href,
				headers: {'Accept': 'application/schema+json'}
			}).then(schema => {
				this.schema = schema.entity;
				return courseCollection;
			});
		}).done(courseCollection => {
			this.setState({
				courses: courseCollection.entity._embedded.courses,
				attributes: Object.keys(this.schema.properties),
				links: courseCollection.entity._links});
		});
	}
	
	onCreate(newStudent) {
		follow(client, root, ['students']).then(studentCollection => {
			return client({
				method: 'POST',
				path: studentCollection.entity._links.self.href,
				entity: newStudent,
				headers: {'Content-Type': 'application/json'}
			})
		}).done(response => {
			this.loadFromServer();
		});
	}
	
	onDelete(student) {
		client({method: 'DELETE', path: student._links.self.href}).done(response => {
			this.loadFromServer();
		});
	}

	componentDidMount() {
		this.loadFromServer();
	}

	render() {
		return (
			<div>
				<CreateDialog attributes={this.state.attributes} onCreate={this.onCreate}/>
				<StudentList  students={this.state.students}
							  courses={this.state.courses}
							  links={this.state.links}
							  onDelete={this.onDelete}/>
			</div>
		)
	}
}

class CreateDialog extends React.Component {

	constructor(props) {
		super(props);
		this.handleSubmit = this.handleSubmit.bind(this);
	}

	handleSubmit(e) {
		e.preventDefault();
		const newStudent = {};
		this.props.attributes.forEach(attribute => {
			newStudent[attribute] = ReactDOM.findDOMNode(this.refs[attribute]).value.trim();
		});
		this.props.onCreate(newStudent);

		// clear out the dialog's inputs
		this.props.attributes.forEach(attribute => {
			ReactDOM.findDOMNode(this.refs[attribute]).value = '';
		});

		// Navigate away from the dialog to hide it.
		window.location = "#";
	}

	render() {
		const inputs = this.props.attributes.map(attribute =>
			<p key={attribute}>
				<input type="text" placeholder={attribute} ref={attribute} className="field"/>
			</p>
		);

		return (
			<div>
				<a href="#createStudent">Add new student</a>

				<div id="createStudent" className="modalDialog">
					<div>
						<a href="#" title="Close" className="close">X</a>

						<h2>Add new student</h2>

						<form>
							{inputs}
							<button onClick={this.handleSubmit}>Add new student</button>
						</form>
					</div>
				</div>
			</div>
		)
	}

}

class StudentList extends React.Component{
	
	constructor(props) {
		super(props);
	}

	render() {
		const students = this.props.students.map(student =>
			<Student key={student._links.self.href} student={student} onDelete={this.props.onDelete}/>
		);
		
		const courses = this.props.courses.map(course =>
			<Course key={course._links.self.href} course={course}/>
		);

		return (
			<div>
				<table>
					<tbody>
						<tr>
							<th>Username</th>
							<th>Full Name</th>
							<th>Email</th>
							<th>CPF</th>
							<th>Address</th>
							<th>Phone</th>
							<th>Civil Status</th>
							<th></th>
						</tr>
						{students}
					</tbody>
				</table>
				
				<table>
					<tbody>
						<tr>
							<th>Course Name</th>
							<th>Course Code</th>
						</tr>
						{courses}
					</tbody>
				</table>
				
			</div>
		)
	}
}

class Student extends React.Component{
	
	constructor(props) {
		super(props);
		this.handleDelete = this.handleDelete.bind(this);
	}
	
	handleDelete() {
		this.props.onDelete(this.props.student);
	}
	
	render() {
		return (
			<tr>
				<td>{this.props.student.username}</td>
				<td>{this.props.student.fullName}</td>
				<td>{this.props.student.email}</td>
				<td>{this.props.student.cpf}</td>
				<td>{this.props.student.address}</td>
				<td>{this.props.student.phone}</td>
				<td>{this.props.student.civilStatus}</td>
				<td>
					<button onClick={this.handleDelete}>Delete</button>
				</td>
			</tr>
		)
	}
}

class Course extends React.Component{
	render() {
		return (
			<tr>
				<td>{this.props.course.coursename}</td>
				<td>{this.props.course.code}</td>
			</tr>
		)
	}
}

ReactDOM.render(
	<App />,
	document.getElementById('react')
)