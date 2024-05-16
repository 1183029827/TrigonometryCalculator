#include <gtk/gtk.h>
#include <stdio.h>
#include <stdlib.h>
#include "callbacks.h"

extern GtkWidget* angle_entry;
extern GtkWidget* terms_entry;
extern GtkWidget* result_label;

void execute_python_script(const char* func) {
    char command[512]; // 用于存储调用 Python 脚本的命令
    FILE* fp;
    char result[1035]; // 用于存储 Python 脚本执行结果的缓冲区

    // 从 GTK 输入框获取角度和项数，并转换为浮点数和整数
    double angle = atof(gtk_entry_get_text(GTK_ENTRY(angle_entry)));
    int terms = atoi(gtk_entry_get_text(GTK_ENTRY(terms_entry)));

    // 准备执行 Python 脚本的命令
    snprintf(command, sizeof(command), "python3 -c \"import TrigCalculator; print(TrigCalculator.%s(%f, %d))\"", func, angle, terms);

    // 打开命令进行读取
    fp = popen(command, "r");
    if (fp == NULL) {
        g_print("运行命令失败\n");
        exit(1);
    }

    // 一次读取一行输出 读取 Python 脚本执行的结果
    if (fgets(result, sizeof(result) - 1, fp) != NULL) {
        // 将读取的结果设置为 GTK 标签的文本
        gtk_label_set_text(GTK_LABEL(result_label), result);
    }

    // 关闭命令
    pclose(fp);
}

void on_calculate_sin(GtkWidget* widget, gpointer data) {
    execute_python_script("calculate_sin_taylor");
}

void on_calculate_cos(GtkWidget* widget, gpointer data) {
    execute_python_script("calculate_cos_taylor");
}

void on_calculate_asin(GtkWidget* widget, gpointer data) {
    execute_python_script("calculate_asin_taylor");
}

void on_calculate_atan(GtkWidget* widget, gpointer data) {
    execute_python_script("calculate_atan_taylor");
}
