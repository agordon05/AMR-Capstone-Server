package com.AMRCapstone.AMRCapstone;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import com.AMRCapstone.AMRCapstone.access.QRAccess;
import com.AMRCapstone.AMRCapstone.access.QR_Queue;
import com.AMRCapstone.AMRCapstone.access.RobotAccess;

@SpringBootApplication
public class AmrCapstoneApplication {

	public static void main(String[] args) {
		QRAccess.initialize();
		QR_Queue.initialize();
		RobotAccess.initialize();

		SpringApplication.run(AmrCapstoneApplication.class, args);
	}

}
