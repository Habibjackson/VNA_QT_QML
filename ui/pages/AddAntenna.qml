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
                        Layout.fillWidth: true
                        id: portsNumber
                    }
                }
                Label {
                    text: qsTr("Ports")
                    font.pixelSize: 16
                    color: theme.textColor
                }
                RowLayout {
                    width: parent.width
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
                            model: portsNumber.value
                            RowLayout {
                                Layout.fillWidth: true
                                CComboBox {
                                    model: ["R1", "Y1", "B1"]
                                    Layout.fillWidth: true
                                }
                                CSpinBox {
                                    Layout.fillWidth: true
                                }
                                CSpinBox {
                                    Layout.fillWidth: true
                                }
                                CComboBox {
                                    Layout.fillWidth: true

                                    model: ['MHz', "Hz", "GHz"]
                                }
                            }
                        }
                    }
                }
                CButton{
                    text: qsTr("Create Antenna")
                }
            }
        }
    }
}
