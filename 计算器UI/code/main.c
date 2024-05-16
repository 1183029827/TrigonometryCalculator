#include <gtk/gtk.h>
#include "callbacks.h"

GtkWidget* angle_entry;
GtkWidget* terms_entry;
GtkWidget* result_label;

int main(int argc, char* argv[]) {
    GtkWidget* window;
    GtkWidget* grid;
    GtkWidget* sin_button, * cos_button, * asin_button, * atan_button;

    gtk_init(&argc, &argv);

    // 创建一个新窗口
    window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    gtk_window_set_title(GTK_WINDOW(window), "三角函数计算器");
    gtk_container_set_border_width(GTK_CONTAINER(window), 10);

    // 创建一个网格并将其附加到窗口上
    grid = gtk_grid_new();
    gtk_container_add(GTK_CONTAINER(window), grid);

    // 创建角度输入
    GtkWidget* angle_label = gtk_label_new("角度");
    gtk_grid_attach(GTK_GRID(grid), angle_label, 0, 0, 1, 1);
    angle_entry = gtk_entry_new();
    gtk_grid_attach(GTK_GRID(grid), angle_entry, 1, 0, 1, 1);

    // 创建项数输入
    GtkWidget* terms_label = gtk_label_new("项数");
    gtk_grid_attach(GTK_GRID(grid), terms_label, 0, 1, 1, 1);
    terms_entry = gtk_entry_new();
    gtk_grid_attach(GTK_GRID(grid), terms_entry, 1, 1, 1, 1);

    // 创建计算按钮
    sin_button = gtk_button_new_with_label("sin");
    g_signal_connect(sin_button, "clicked", G_CALLBACK(on_calculate_sin), NULL);
    gtk_grid_attach(GTK_GRID(grid), sin_button, 0, 2, 1, 1);

    cos_button = gtk_button_new_with_label("cos");
    g_signal_connect(cos_button, "clicked", G_CALLBACK(on_calculate_cos), NULL);
    gtk_grid_attach(GTK_GRID(grid), cos_button, 1, 2, 1, 1);

    asin_button = gtk_button_new_with_label("asin");
    g_signal_connect(asin_button, "clicked", G_CALLBACK(on_calculate_asin), NULL);
    gtk_grid_attach(GTK_GRID(grid), asin_button, 2, 2, 1, 1);

    atan_button = gtk_button_new_with_label("atan");
    g_signal_connect(atan_button, "clicked", G_CALLBACK(on_calculate_atan), NULL);
    gtk_grid_attach(GTK_GRID(grid), atan_button, 3, 2, 1, 1);

    // 创建结果标签
    result_label = gtk_label_new("");
    gtk_grid_attach(GTK_GRID(grid), result_label, 0, 3, 4, 1);

    // 连接窗口关闭事件
    g_signal_connect(window, "destroy", G_CALLBACK(gtk_main_quit), NULL);

    // 显示所有窗口部件
    gtk_widget_show_all(window);

    // 运行GTK主循环
    gtk_main();

    return 0;
}
