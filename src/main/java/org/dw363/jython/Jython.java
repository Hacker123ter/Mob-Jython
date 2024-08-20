package org.dw363.jython;

import org.bukkit.plugin.java.JavaPlugin;
import org.python.util.PythonInterpreter;
import org.python.core.PyObject;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.BufferedReader;

public class Jython extends JavaPlugin {
    private PythonInterpreter interpreter;
    @Override
    public void onEnable() {
        try {
            interpreter = new PythonInterpreter();
            InputStream inputStream = getResource("python/file.py");
            if (inputStream == null) {
                return;
            }
            BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream));
            StringBuilder script = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                script.append(line).append("\n");
            }
            reader.close();
            interpreter.exec(script.toString());
            PyObject mainFunc = interpreter.get("main");
            if (mainFunc != null) {
                mainFunc.__call__();
                getLogger().info("Скрипт Python загружен!");
            } else {
                getLogger().warning("В скрипте Python не найдена «main» функция.");
            }
        } catch (Exception e) {
            getLogger().severe("Ошибка выполнения скрипта Python: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
