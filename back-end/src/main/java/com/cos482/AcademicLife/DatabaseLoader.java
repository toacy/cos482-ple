package com.cos482.AcademicLife;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

@Component
public class DatabaseLoader implements CommandLineRunner {

	private final StudentRepository students;
	private final CourseRepository courses;

	@Autowired
	public DatabaseLoader(StudentRepository studentRepository,
						  CourseRepository courseRepository) {
		
		this.students = studentRepository;
		this.courses = courseRepository;
	}

	@Override
	public void run(String... strings) throws Exception {
		this.students.save(new Student("user1", "Nome de Exemplo", "a@gmail.com", "11111111111", "A", "111111111", "A"));
		this.students.save(new Student("user2", "Nome de Exemplo2", "b@gmail.com", "22222222222", "B", "222222222", "B"));
		this.courses.save(new Course("Qualidade de Software", "COS482"));
		this.courses.save(new Course("aaaaaa", "AAA000"));
	}
}
