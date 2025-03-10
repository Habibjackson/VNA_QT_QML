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
                    }
                }
                Label {
                    text: qsTr("Ports")
                    font.pixelSize: 16
                    color: theme.textColor
                }
                Rectangle {
                    Layout.fillWidth: true
                    ColumnLayout {
                        width: parent.width
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
                            Layout.fillWidth: true
                            Layout.fillHeight: true
                            Repeater {
                                model: 12
                                delegate: RowLayout {
                                    width: parent.width
                                    CComboBox {
                                        model: ["R", "Y", "B"]
                                    }

                                    CSpinBox {
                                        id: minFrequency
                                        Layout.fillWidth: true
                                    }

                                    CSpinBox {
                                        id: maxFrequency
                                        Layout.fillWidth: true
                                    }

                                    CComboBox {
                                        Layout.fillWidth: true
                                        model: ["Hz", "MHz", "GHz"]
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

// import QtQuick
// import QtQuick.Layouts
// import QtQuick.Controls.Material
// import "../Components"
// import "../Widgets"

// Paper {
//     id: manageAntenna
//     ColumnLayout {
//         spacing: 10
//         height: parent.height
//         width: parent.width

//         TitleBar {
//             Layout.fillWidth: true
//             color: "#003d01"
//             title: qsTr("Add Antenna")
//         }

//         Item {
//             Layout.fillHeight: true
//             Layout.fillWidth: true
//             Layout.margins: 14
//             ColumnLayout {
//                 width: parent.width
//                 spacing: 8

//                 RowLayout {
//                     Layout.fillWidth: true
//                     Label {
//                         text: qsTr("Model Name")
//                         color: theme.textColor
//                         Layout.preferredWidth: 100
//                     }
//                     CTextField {
//                         id: modelName
//                         Layout.fillWidth: true
//                     }
//                 }

//                 RowLayout {
//                     Layout.fillWidth: true
//                     Label {
//                         text: qsTr("Number of ports")
//                         color: theme.textColor
//                         Layout.preferredWidth: 100
//                     }
//                     CSpinBox {
//                         id: numPorts
//                         Layout.fillWidth: true
//                         from: 1
//                         to: 10
//                         value: 1
//                     }
//                 }
//                 ColumnLayout {
//                     Layout.fillWidth: true
//                     Layout.fillHeight: true

//                     Label {
//                         text: qsTr("Ports")
//                         font.pixelSize: 16
//                         color: theme.textColor
//                     }

//                     // Scrollable container for dynamic rows
//                     ScrollView {
//                         Layout.fillWidth: true
//                         Layout.fillHeight: true
//                         clip: true

//                         contentHeight: columnRepeater.height
//                         ScrollBar.vertical.policy: ScrollBar.AlwaysOn

//                         Column {
//                             id: columnRepeater
//                             width: parent.width
//                             spacing: 8

//                             // Header Row (Fixed Labels)
//                             RowLayout {
//                                 width: parent.width
//                                 spacing: 10

//                                 Label {
//                                     text: "Port"
//                                     color: theme.textColorSecondary
//                                     Layout.fillWidth: true
//                                 }
//                                 Label {
//                                     text: "Min"
//                                     color: theme.textColorSecondary
//                                     Layout.fillWidth: true
//                                 }
//                                 Label {
//                                     text: "Max"
//                                     color: theme.textColorSecondary
//                                     Layout.fillWidth: true
//                                 }
//                                 Label {
//                                     text: "Unit"
//                                     color: theme.textColorSecondary
//                                     Layout.fillWidth: true
//                                 }
//                             }

//                             // Dynamic Rows
//                             Repeater {
//                                 id: repeater
//                                 model: 12 // Max rows (Can be dynamically adjusted)

//                                 delegate: RowLayout {
//                                     width: parent.width
//                                     spacing: 10

//                                     ComboBox {
//                                         model: ["R", "Y", "B"]
//                                         Layout.fillWidth: true
//                                     }

//                                     SpinBox {
//                                         id: minFrequency
//                                         Layout.fillWidth: true
//                                     }

//                                     SpinBox {
//                                         id: maxFrequency
//                                         Layout.fillWidth: true
//                                     }

//                                     ComboBox {
//                                         model: ["Hz", "MHz", "GHz"]
//                                         Layout.fillWidth: true
//                                     }
//                                 }
//                             }
//                         }
//                     }

//                     // Button to generate Antenna file
//                     Button {
//                         text: "Generate Antenna File"
//                         Layout.alignment: Qt.AlignRight
//                         onClicked: {
//                             console.log("Generating Antenna File...");
//                         }
//                     }
//                 }
//             }
//         }
//     }
// }
