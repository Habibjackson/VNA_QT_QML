import QtQuick
import QtQuick.Controls.Material
import QtQuick.Layouts

Dialog {
    id: antennaDialog
    title: "Add Antenna"
    modal: true
    width: 400
    standardButtons: Dialog.Ok | Dialog.Cancel

    ColumnLayout {
        anchors.fill: parent
        spacing: 10

        TextField {
            id: modelNameField
            Layout.fillWidth: true
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

    onAccepted: {
        let portData = []
        for (var i = 0; i < portCount.value; i++) {
            let portType = portsContainer.children[i].children[1].currentText
            portData.push(portType)
        }
        antennaManager.addAntenna(modelNameField.text,
                                  portCount.value, portData)
    }

    function generatePorts() {
        portsContainer.children = []

        for (var i = 0; i < portCount.value; i++) {
            portsContainer.children.push(createPortField(i + 1))
        }
    }

    function createPortField(portNumber) {
        return Qt.createQmlObject(`
                                  RowLayout {
                                  spacing: 10

                                  Label { text: "Port " + ${portNumber} + ":" }

                                  ComboBox {
                                  model: ["SMA", "N-Type", "BNC", "TNC"]
                                  currentIndex: 0
                                  }
                                  }
                                  `, portsContainer)
    }
}
