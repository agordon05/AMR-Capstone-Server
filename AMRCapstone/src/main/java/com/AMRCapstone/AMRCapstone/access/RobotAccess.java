package com.AMRCapstone.AMRCapstone.access;

import java.util.ArrayList;

import com.AMRCapstone.AMRCapstone.model.Robot;

public class RobotAccess {
    private static Robot robot;

    public static void initialize() {
        // QR_Codes = new ArrayList<QR>();
        robot = loadRobot();
    }

    private static Robot loadRobot() {
        // TEMPORARY
        float x_dest = QR_Queue.getCurrentQR().getX_pos();
        float y_dest = QR_Queue.getCurrentQR().getY_pos();

        robot = new Robot(1, "Inactive", "Connecting", 1, 1, 0, x_dest, y_dest, null, new ArrayList<String>(), null);
        robot.addtoLoggerList("Waiting for robot to connect");
        // robot.setUserSignal("Forward");
        return robot;
    }

    public static Robot getRobot() {
        return robot;
    }
}
