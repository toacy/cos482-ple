package com.cos482.AcademicLife;

import java.util.Objects;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;

@Entity
public class Course {

	private @Id @GeneratedValue Long id;
	private String coursename;
	private String code;

	private Course() {}

	public Course(String coursename, String code) {
		this.coursename = coursename;
		this.code = code;
	}

	@Override
	public boolean equals(Object o) {
		if (this == o) return true;
		if (o == null || getClass() != o.getClass()) return false;
		Course course = (Course) o;
		return Objects.equals(id, course.id) &&
			Objects.equals(coursename, course.coursename) &&
			Objects.equals(code, course.code);
	}

	@Override
	public int hashCode() {

		return Objects.hash(id, coursename, code);
	}

	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	public String getCoursename() {
		return coursename;
	}

	public void setFirstName(String coursename) {
		this.coursename = coursename;
	}

	public String getCode() {
		return code;
	}

	public void setCode(String code) {
		this.code = code;
	}

	@Override
	public String toString() {
		return "Course{" +
			"id=" + id +
			", coursename='" + coursename + '\'' +
			", code='" + code + '\'' +
			'}';
	}
}
