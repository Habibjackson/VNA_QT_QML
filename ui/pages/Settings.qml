import QtQuick
import QtQuick.Controls.Material
import QtQuick.Layouts
import "../widgets"
import "../Components"

Paper {
    id: settings
    ColumnLayout {
        anchors.fill: parent
        spacing: 10
        anchors.margins: 10

        // Storage Directory
        RowLayout {
            Label {
                Layout.fillWidth: true
                color: theme.textColor
                text: "Storage"
                font.pointSize: 12
                font.bold: true
            }
            TextField {
                color: theme.textColor
                text: settingsManager.directory
                Layout.fillWidth: true
                onTextChanged: settingsManager.directory = text
            }
        }

        // Serial Port Selection
        ColumnLayout {
            RowLayout {
                Label {
                    Layout.fillWidth: true
                    color: theme.textColor
                    text: "RET Controller"
                    font.pointSize: 12
                    font.bold: true
                }
                ComboBox {
                    id: serialPortCombo
                    model: settingsManager.serialPortsModel
                    onCurrentTextChanged: settingsManager.serialPort = currentText
                    Layout.fillWidth: true
                    currentIndex: {
                        if (model && settingsManager.serialPort) {
                            var index = model.stringList().indexOf(settingsManager.serialPort);
                            return index >= 0 ? index : 0;
                        }
                        return 0; // Default to first item if undefined or not found
                    }
                }
                Button {
                    text: "Refresh"
                    onClicked: settingsManager.refreshSerialPorts()
                }
            }
            RowLayout {
                Layout.fillWidth: true
                Label {
                    Layout.fillWidth: true
                    color: theme.textColor
                    text: "Switch"
                    font.pointSize: 12
                    font.bold: true
                }
                ComboBox {
                    id: switchPort
                    model: settingsManager.serialPortsModel
                    onCurrentTextChanged: settingsManager.serialPort = currentText
                    Layout.fillWidth: true
                    currentIndex: {
                        if (model && settingsManager.serialPort) {
                            var index = model.stringList().indexOf(settingsManager.serialPort);
                            return index >= 0 ? index : 0;
                        }
                        return 0; // Default to first item if undefined or not found
                    }
                }
                Button {
                    text: "Refresh"
                    onClicked: settingsManager.refreshSerialPorts()
                }
            }
        }

        // Reset Button
        Button {
            text: "Reset to Defaults"
            onClicked: {
                settingsManager.windowWidth = 800;
                settingsManager.windowHeight = 600;
                settingsManager.directory = "/default/path";
                settingsManager.serialPort = "COM1";
            }
        }
    }

    Connections {
        target: settingsManager
        function onSerialDataReceived(data) {
            serialDataArea.append(data);
        }
    }
}
