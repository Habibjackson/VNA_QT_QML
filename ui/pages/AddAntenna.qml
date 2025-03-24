import QtQuick
import QtQuick.Layouts
import QtQuick.Dialogs
import QtQuick.Controls.Material
import "../Components"
import "../Widgets"

Paper {
    id: manageAntenna
    // anchors.fill: parent
    ColumnLayout {
        spacing: 10
        height: parent.height
        width: parent.width
        TitleBar {
            Layout.fillWidth: true
            color: "#003d01"
            title: qsTr("Add Antenna")
        }
        Item {
            Layout.fillHeight: true
            Layout.fillWidth: true
            Layout.margins: 14
            ColumnLayout {
                width: parent.width
                height: parent.height
                spacing: 8
                CButton {
                    Layout.fillWidth: true
                    text: qsTr("Upload Data Sheet")
                    onClicked: fileDialog.open()
                }
                FileDialog {
                    id: fileDialog
                    title: "Select a datasheet"
                    nameFilters: ["document (*.pdf)"]
                    // selectMultiple: false
                    onAccepted: {
                        antennaManager.parseAntennaFromDatasheet(selectedFile);
                        // You can use fileUrl to load the file or pass it to backend functions.
                    }
                    onRejected: {
                        console.log("File selection was canceled.");
                    }
                }

                CLine {
                    Layout.fillWidth: true
                    height: 30
                    text: "OR"
                }
                RowLayout {
                    Layout.fillWidth: true
                    Label {
                        text: qsTr("Model Name")
                        color: theme.textColor
                        Layout.preferredWidth: 100
                    }
                    CTextField {
                        Layout.fillWidth: true
                    }
                }
                RowLayout {
                    Layout.fillWidth: true
                    Label {
                        text: qsTr("Number of ports")
                        color: theme.textColor
                        Layout.preferredWidth: 100
                    }
                    CSpinBox {
                        id: portsNumber
                        Layout.fillWidth: true
                    }
                }
                Label {
                    text: qsTr("Ports")
                    font.pixelSize: 16
                    color: theme.textColor
                }
                RowLayout {
                    Layout.preferredWidth: parent.width
                    Label {
                        Layout.fillWidth: true
                        text: qsTr("Port")
                        color: theme.textColorSecondary
                    }

                    Label {
                        Layout.fillWidth: true
                        text: qsTr("Min")
                        color: theme.textColorSecondary
                    }

                    Label {
                        Layout.fillWidth: true
                        text: qsTr("Max")
                        color: theme.textColorSecondary
                    }

                    Label {
                        Layout.fillWidth: true
                        text: qsTr("Unit")
                        color: theme.textColorSecondary
                    }
                }
                ScrollView {
                    Layout.fillHeight: true
                    Layout.fillWidth: true
                    ColumnLayout {
                        id: portList
                        width: parent.width
                        spacing: 4
                        Repeater {
                            id: repeater
                            model: portsNumber.value
                            RowLayout {
                                property alias port: combo1
                                property alias min: spinBox1
                                property alias max: spinBox2
                                property alias unit: combo2

                                Layout.fillWidth: true
                                CComboBox {
                                    id: combo1
                                    model: ["R1", "Y1", "B1"]
                                    Layout.fillWidth: true
                                }
                                CSpinBox {
                                    id: spinBox1
                                    Layout.fillWidth: true
                                }
                                CSpinBox {
                                    id: spinBox2
                                    Layout.fillWidth: true
                                }
                                CComboBox {
                                    id: combo2
                                    Layout.fillWidth: true
                                    model: ['MHz', "Hz", "GHz"]
                                }
                            }
                        }
                    }
                }
                CButton {
                    text: qsTr("Create Antenna")
                    onClicked: {
                        var data = {
                            "port info": {}
                        };
                        for (var i = 0; i < repeater.count; i++) {
                            var item = repeater.itemAt(i);
                            if (item) {}
                        }
                        var jsonString = JSON.stringify(data, null, 2);
                        console.log(jsonString); // Print JSON to console
                        antennaManager.saveAntenna("2523.ant", data);

                        // You can send jsonString to C++ or save it to a file
                    }
                }
            }
        }
    }
}
