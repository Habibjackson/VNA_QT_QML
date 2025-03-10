import QtQuick
import QtQuick.Layouts
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
            Layout.alignment: Qt.AlignTop
            color: "#003d01"
            title: qsTr("Add Antenna")
        }

        ColumnLayout {
            Layout.fillHeight: true
            Layout.fillWidth: true
            spacing: 10

            TextField {
                id: modelNameField
                Layout.fillWidth: true
                color: theme.textColor
                placeholderText: "Enter Model Name"
            }

            RowLayout {
                spacing: 10

                Label {
                    text: "Number of Ports:"
                }

                SpinBox {
                    id: portCount
                    from: 1
                    to: 10
                    value: 1
                    onValueChanged: generatePorts()
                }
            }

            Column {
                id: portsContainer
                Layout.fillWidth: true
                spacing: 5
            }
        }

        RowLayout {
            CButton {
                text: "Back"
                icon.source: "\u0003c"
                // onClicked: pageContent.mainStack.pop()
            }
        }
    }
}
