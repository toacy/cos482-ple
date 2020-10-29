package com.cos482.AcademicLife;

import java.util.Objects;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;

@Entity
public class Student {

	private @Id @GeneratedValue Long id;
	private String username;
	private String fullName;
	private String email;
	private String cpf;
	private String address;
	private String phone;
	private String civilStatus;

	private Student() {}

	public Student(String username, String fullName, String email, String cpf, String address, String phone, String civilStatus) {
		this.username = username;
		this.fullName = fullName;
		this.email = email;
		this.cpf = cpf;
		this.address = address;
		this.phone = phone;
		this.civilStatus = civilStatus;
	}

	@Override
	public boolean equals(Object o) {
		if (this == o) return true;
		if (o == null || getClass() != o.getClass()) return false;
		Student employee = (Student) o;
		return Objects.equals(id, employee.id) &&
			Objects.equals(username, employee.username) &&
			Objects.equals(fullName, employee.fullName) &&
			Objects.equals(email, employee.email) &&
			Objects.equals(cpf, employee.cpf) &&
			Objects.equals(address, employee.address) &&
			Objects.equals(phone, employee.phone) &&
			Objects.equals(civilStatus, employee.civilStatus);
	}

	@Override
	public int hashCode() {

		return Objects.hash(id, username, fullName, email, cpf, address, phone, civilStatus);
	}

	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	public String getUsername() {
		return username;
	}

	public void setFirstName(String username) {
		this.username = username;
	}

	public String getFullName() {
		return fullName;
	}

	public void setFullName(String fullName) {
		this.fullName = fullName;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}
	
	public String getCpf() {
		return cpf;
	}

	public void setCpf(String cpf) {
		this.cpf = cpf;
	}
	
	public String getAddress() {
		return address;
	}

	public void setAddress(String address) {
		this.address = address;
	}
	
	public String getPhone() {
		return phone;
	}

	public void setPhone(String phone) {
		this.phone = phone;
	}

	public String getCivilStatus() {
		return civilStatus;
	}

	public void setCivilStatus(String civilStatus) {
		this.civilStatus = civilStatus;
	}

	@Override
	public String toString() {
		return "Employee{" +
			"id=" + id +
			", username='" + username + '\'' +
			", fullName='" + fullName + '\'' +
			", email='" + email + '\'' +
			", cpf='" + cpf + '\'' +
			", address='" + address + '\'' +
			", phone='" + phone + '\'' +
			", civilStatus='" + civilStatus + '\'' +
			'}';
	}
}
