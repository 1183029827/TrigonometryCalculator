#ifndef CALLBACKS_H
#define CALLBACKS_H

#include <gtk/gtk.h>

extern GtkWidget* angle_entry;
extern GtkWidget* terms_entry;
extern GtkWidget* result_label;

void execute_python_script(const char* func);
void on_calculate_sin(GtkWidget* widget, gpointer data);
void on_calculate_cos(GtkWidget* widget, gpointer data);
void on_calculate_asin(GtkWidget* widget, gpointer data);
void on_calculate_atan(GtkWidget* widget, gpointer data);

#endif
