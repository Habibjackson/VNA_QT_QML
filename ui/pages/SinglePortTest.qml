import QtQuick
import QtQuick.Controls.Material
import QtQuick.Layouts
import "../Components"
import "../Widgets"

Paper {
    id: testsPage
    ColumnLayout {
        spacing: 10
        height: parent.height
        width: parent.width

        TitleBar {
            Layout.fillWidth: true
            color: "#360d2d"
            title: "Single Port Testing"
        }
        Item {
            Layout.fillWidth: true
            Layout.fillHeight: true
            Layout.margins: 12
            ColumnLayout {
                width: parent.width
                RowLayout {
                    Layout.fillWidth: true
                    Label {
                        text: qsTr("Antenna Model")
                        color: theme.textColor
                    }
                    CComboBox {
                        Layout.fillWidth: true
                        model: ["Antenna1", "Antenna2"]
                    }
                }
                RowLayout {
                    Label {
                        text: qsTr("Description")
                        color: theme.textColor
                    }
                    CTextField {
                        Layout.fillWidth: true
                    }
                }
            }
        }
        CButton {
            text: qsTr("Back")
            onClicked: pageContent.mainStack.pop()
        }
    }
}
